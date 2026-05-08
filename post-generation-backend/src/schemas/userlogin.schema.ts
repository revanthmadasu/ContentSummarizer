import { Prop, Schema, SchemaFactory } from "@nestjs/mongoose";

@Schema()
export class UserLogin {
  @Prop({ required: true, unique: true })
  email: string;
  @Prop({ required: true })
  passwordHash: string;
}

export class UserLoginDto {
  readonly email: string;
  readonly password: string;
}

export const UserLoginSchema = SchemaFactory.createForClass(UserLogin);