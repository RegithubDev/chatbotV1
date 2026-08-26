import { Module } from '@nestjs/common';
import { SchemaModule } from '../schema/schema.module';
import { DbModule } from '../db/db.module';
import { AskController } from './ask.controller';
import { AskService } from './ask.service';

@Module({
  imports: [DbModule, SchemaModule],
  controllers: [AskController],
  providers: [AskService],
})
export class AskModule {}
