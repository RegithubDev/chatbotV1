import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  root() {
    return {
      service: 'Recollect AI Bot',
      motto: 'Ask your database. Get the answer.',
      routes: ['GET /health', 'GET /schema/stats', 'POST /schema/refresh', 'POST /ask'],
    };
  }

  @Get('health')
  health() {
    return { ok: true, service: 'Recollect AI Bot', time: new Date().toISOString() };
  }
}
