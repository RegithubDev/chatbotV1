import { Injectable, OnModuleDestroy } from '@nestjs/common';
import * as mysql from 'mysql2/promise';

@Injectable()
export class DbService implements OnModuleDestroy {
  private pool: mysql.Pool | null = null;

  private getPool() {
    if (!this.pool) {
      this.pool = mysql.createPool({
        host: process.env.DB_HOST || 'localhost',
        port: Number(process.env.DB_PORT || 3306),
        user: process.env.DB_USER,
        password: process.env.DB_PASSWORD,
        database: process.env.DB_NAME,
        waitForConnections: true,
        connectionLimit: 10,
        namedPlaceholders: true,
      });
    }
    return this.pool;
  }

  async query<T = any>(sql: string, params: any[] | Record<string, any> = []): Promise<T[]> {
    const [rows] = await this.getPool().query(sql, params);
    return rows as T[];
  }

  async onModuleDestroy() {
    if (this.pool) await this.pool.end();
  }
}
