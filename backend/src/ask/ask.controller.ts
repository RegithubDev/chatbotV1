import { Body, Controller, Post } from '@nestjs/common';
import { AskService } from './ask.service';

@Controller('ask')
export class AskController {
  constructor(private readonly ask: AskService) {}

  @Post()
  handle(@Body() body: { question?: string }) {
    return this.ask.ask(body?.question || '');
  }
}
