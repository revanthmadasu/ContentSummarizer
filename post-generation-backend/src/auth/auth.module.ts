import { Module } from '@nestjs/common';
import { AuthController } from './auth.controller';
import { AuthService } from './auth.service';
import { MongooseModule } from '@nestjs/mongoose';
import { UserLogin, UserLoginSchema } from 'src/schemas/userlogin.schema';
import { JwtModule } from '@nestjs/jwt';
import { JWT_SECRET } from 'src/constants';

@Module({
  imports: [
    MongooseModule.forFeature([{name: UserLogin.name, schema: UserLoginSchema}]),
    JwtModule.register({
      global: true, 
      secret: JWT_SECRET
    })
  ],
  controllers: [AuthController],
  providers: [AuthService]
})
export class AuthModule {}
