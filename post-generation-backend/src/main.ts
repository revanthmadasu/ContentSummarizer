import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { ConsoleLogger, Logger } from '@nestjs/common';

async function bootstrap() {
  const app = await NestFactory.create(AppModule, {
    logger: new ConsoleLogger({
      logLevels: ['log', 'error', 'debug', 'warn'],
      colors: true,
      prefix: "User-feed-service"
    })
  });
  await app.listen(process.env.PORT ?? 3000);
  Logger.log(`mrk - Server is running on port ${process.env.PORT ?? 3000}`);
  console.log(`mrk - Server is running on port ${process.env.PORT ?? 3000}`);
}
bootstrap();
