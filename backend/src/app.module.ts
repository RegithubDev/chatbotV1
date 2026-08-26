import { Module } from '@nestjs/common';
import { DbModule } from './db/db.module';
import { SchemaModule } from './schema/schema.module';
import { AskModule } from './ask/ask.module';
import { AppController } from './app.controller';
import { AppService } from './app.service';

@Module({
  imports: [DbModule, SchemaModule, AskModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
