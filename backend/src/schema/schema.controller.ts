import { Controller, Get, Post } from '@nestjs/common';
import { SchemaCatalogService } from './schema-catalog.service';

@Controller('schema')
export class SchemaController {
  constructor(private readonly catalog: SchemaCatalogService) {}

  @Post('refresh')
  refresh() {
    return this.catalog.refresh();
  }

  @Get('stats')
  stats() {
    return this.catalog.stats();
  }

  @Get('tables')
  tables() {
    return this.catalog.listTables();
  }
}
