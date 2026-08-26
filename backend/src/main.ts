import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import * as dotenv from 'dotenv';
import * as path from 'path';

dotenv.config({ path: path.join(__dirname, '..', '.env') });
dotenv.config({ path: path.join(__dirname, '..', '..', '.env') });

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.enableCors({ origin: true });
  const port = Number(process.env.PORT || 3000);
  await app.listen(port);
  console.log(`Recollect AI Bot API listening on http://localhost:${port}`);
  console.log('Routes: GET /health  GET /schema/stats  POST /schema/refresh  POST /ask');
}
bootstrap();
