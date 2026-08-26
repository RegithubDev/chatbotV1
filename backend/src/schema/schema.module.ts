import { Module } from '@nestjs/common';
import { DbModule } from '../db/db.module';
import { SchemaCatalogService } from './schema-catalog.service';
import { SchemaController } from './schema.controller';

@Module({
  imports: [DbModule],
  controllers: [SchemaController],
  providers: [SchemaCatalogService],
  exports: [SchemaCatalogService],
})
export class SchemaModule {}
