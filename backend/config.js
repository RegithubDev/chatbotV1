const path = require("path");
require("dotenv").config({ path: path.join(__dirname, ".env") });
require("dotenv").config({ path: path.join(__dirname, "..", ".env") });

const config = {
  db: {
    host: process.env.DB_HOST || "localhost",
    port: Number(process.env.DB_PORT || 3306),
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME || "recollect-local",
  },
  groq: {
    apiKey: process.env.GROQ_API_KEY,
    model: process.env.GROQ_MODEL || "qwen/qwen3.8-27b",
  },
  ollama: {
    url: process.env.OLLAMA_URL || "http://127.0.0.1:11434",
    model: process.env.CHAT_MODEL || process.env.SQL_MODEL || "qwen2.5-coder:7b-instruct",
  },
  port: Number(process.env.PORT || 3020),
};

module.exports = config;
