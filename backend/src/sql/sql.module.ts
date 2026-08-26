import { Module } from '@nestjs/common';
import { SqlGeneratorService } from './sql-generator.service';
import { SqlValidatorService } from './sql-validator.service';
import { SqlExecutorService } from './sql-executor.service';

@Module({
  providers: [SqlGeneratorService, SqlValidatorService, SqlExecutorService]
})
export class SqlModule {}
