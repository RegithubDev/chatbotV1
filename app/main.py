from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.ai.answer_generator import generate_answer
from app.ai.schema_embeddings import build_embeddings
from app.ai.sql_generator import generate_sql
from app.ai.sql_validator import validate_sql
from app.ai.schema_search import search_schema
from app.ai.ollama_client import generate
from app.ai.answer_formatter import format_answer
from app.ai.answer_formatter import format_answer

from app.database.connector import (
    create_mysql_engine,
    test_connection
)

from app.database.schema_reader import (
    read_schema
)

from app.database.query_executor import (
    execute_select
)

from app.storage.schema_store import (
    save_schema,
    load_schema
)


app = FastAPI(
    title="Recollect AI Bot",
    version="0.1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# DATABASE CONNECTION MODEL
# ============================================================

class DatabaseConnection(BaseModel):

    host: str

    port: int = 3306

    database: str

    username: str

    password: str


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():

    return {
        "application": "Recollect AI Bot",
        "status": "running"
    }


# ============================================================
# HEALTH
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "ok"
    }


# ============================================================
# TEST DATABASE CONNECTION
# ============================================================

@app.post("/api/database/test")
def database_test(
    request: DatabaseConnection
):

    try:

        engine = create_mysql_engine(
            host=request.host,
            port=request.port,
            database=request.database,
            username=request.username,
            password=request.password
        )

        connected = test_connection(
            engine
        )

        return {
            "success": connected,
            "message": (
                "Database connection successful"
                if connected
                else
                "Database connection failed"
            )
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# ============================================================
# READ COMPLETE DATABASE SCHEMA
# ============================================================

@app.post("/api/database/schema")
def database_schema(
    request: DatabaseConnection
):

    try:

        engine = create_mysql_engine(
            host=request.host,
            port=request.port,
            database=request.database,
            username=request.username,
            password=request.password
        )

        schema = read_schema(
            engine,
            request.database
        )

        return {
            "success": True,
            "schema": schema
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# ============================================================
# DATABASE SCHEMA SUMMARY
# ============================================================

@app.post("/api/database/schema/summary")
def database_schema_summary(
    request: DatabaseConnection
):

    try:

        engine = create_mysql_engine(
            host=request.host,
            port=request.port,
            database=request.database,
            username=request.username,
            password=request.password
        )

        schema = read_schema(
            engine,
            request.database
        )

        tables = schema.get(
            "tables",
            []
        )

        relationships = schema.get(
            "relationships",
            []
        )

        summary = []

        for table in tables:

            summary.append({

                "table": table[
                    "table_name"
                ],

                "column_count": len(
                    table.get(
                        "columns",
                        []
                    )
                ),

                "columns": [
                    column["name"]
                    for column in table.get(
                        "columns",
                        []
                    )
                ],

                "primary_key": table.get(
                    "primary_key",
                    []
                ),

                "foreign_key_count": len(
                    table.get(
                        "foreign_keys",
                        []
                    )
                )

            })

        return {

            "success": True,

            "database": schema.get(
                "database"
            ),

            "table_count": len(
                tables
            ),

            "relationship_count": len(
                relationships
            ),

            "tables": summary,

            "relationships": relationships

        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# ============================================================
# SAVE DATABASE SCHEMA
# ============================================================

@app.post("/api/database/schema/save")
def save_database_schema(
    request: DatabaseConnection
):

    try:

        engine = create_mysql_engine(
            host=request.host,
            port=request.port,
            database=request.database,
            username=request.username,
            password=request.password
        )

        schema = read_schema(
            engine,
            request.database
        )

        database_name = schema.get(
            "database"
        )

        if not database_name:

            raise Exception(
                "Unable to determine database name"
            )

        file_path = save_schema(
            database_name,
            schema
        )

        return {

            "success": True,

            "database": database_name,

            "table_count": len(
                schema.get(
                    "tables",
                    []
                )
            ),

            "relationship_count": len(
                schema.get(
                    "relationships",
                    []
                )
            ),

            "saved_to": file_path

        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# ============================================================
# LOAD SAVED SCHEMA
# ============================================================

@app.get(
    "/api/database/schema/{database_name}"
)
def get_saved_schema(
    database_name: str
):

    try:

        schema = load_schema(
            database_name
        )

        if schema is None:

            raise HTTPException(
                status_code=404,
                detail=(
                    f"No saved schema found "
                    f"for database '{database_name}'"
                )
            )

        return {

            "success": True,

            "schema": schema

        }

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ============================================================
# TEST OLLAMA
# ============================================================

@app.get("/api/ai/test")
def ai_test():

    try:

        response = generate(
            "Return only the word OK"
        )

        return {

            "success": True,

            "response": response

        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ============================================================
# BUILD DATABASE EMBEDDINGS
# ============================================================

@app.post("/api/database/schema/embed")
def embed_database_schema(
    request: DatabaseConnection
):

    try:

        engine = create_mysql_engine(
            host=request.host,
            port=request.port,
            database=request.database,
            username=request.username,
            password=request.password
        )

        schema = read_schema(
            engine,
            request.database
        )

        result = build_embeddings(
            schema
        )

        return {
            "success": True,
            "database": request.database,
            "result": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ============================================================
# SQL GENERATION
# ============================================================

class SQLGenerationRequest(BaseModel):

    question: str

    top_k: int = 5


@app.post("/api/ai/sql")
def generate_database_sql(
    request: SQLGenerationRequest
):

    try:

        search_results = search_schema(
            request.question,
            request.top_k
        )

        if not search_results:

            raise HTTPException(
                status_code=404,
                detail=(
                    "No relevant database schema "
                    "was found"
                )
            )

        sql = generate_sql(
            request.question,
            search_results
        )

        validation = validate_sql(
            sql
        )

        return {

            "success": validation["valid"],

            "question":
                request.question,

            "sql":
                validation.get(
                    "sql",
                    sql
                ),

            "validation":
                validation,

            "schema_results":
                search_results

        }

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ============================================================
# SCHEMA SEARCH
# ============================================================

class SchemaSearchRequest(BaseModel):

    question: str

    top_k: int = 5


@app.post("/api/database/schema/search")
def search_database_schema(
    request: SchemaSearchRequest
):

    try:

        results = search_schema(
            request.question,
            request.top_k
        )

        return {
            "success": True,
            "question": request.question,
            "results": results
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ============================================================
# DATABASE AI QUERY
# ============================================================

class DatabaseQueryRequest(BaseModel):

    host: str

    port: int = 3306

    database: str

    username: str

    password: str

    question: str


@app.post("/api/ai/query")
def execute_database_question(
    request: DatabaseQueryRequest
):

    try:

        # ====================================================
        # 1. CONNECT TO REAL DATABASE
        # ====================================================

        engine = create_mysql_engine(
            host=request.host,
            port=request.port,
            database=request.database,
            username=request.username,
            password=request.password
        )

        question = request.question.strip()

        if not question:

            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty"
            )

        # ====================================================
        # 2. SEARCH REAL DATABASE SCHEMA
        # ====================================================

        search_results = search_schema(
            question,
            5
        )

        if not search_results:

            raise HTTPException(
                status_code=404,
                detail="No relevant database schema found"
            )

        # ====================================================
        # 3. GENERATE SQL
        # ====================================================

        sql = generate_sql(
            question,
            search_results
        )

        # ====================================================
        # 4. VALIDATE SQL
        # ====================================================

        validation = validate_sql(
            sql
        )

        if not validation["valid"]:

            raise HTTPException(
                status_code=400,
                detail=validation
            )

        safe_sql = validation["sql"]

        # ====================================================
        # 5. EXECUTE AGAINST REAL MYSQL
        # ====================================================

        result = execute_select(
            engine,
            safe_sql
        )

        # ====================================================
        # 6. FORMAT ACTUAL DATABASE DATA
        # ====================================================

        answer = format_database_answer(
            question,
            result
        )

        # ====================================================
        # 7. RETURN
        # ====================================================

        return {

            "success": True,

            "question": question,

            "answer": answer,

            "sql": safe_sql,

            "result": result,

            "row_count": result.get(
                "row_count",
                0
            )

        }

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
