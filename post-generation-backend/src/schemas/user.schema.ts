import { Prop, Schema, SchemaFactory } from "@nestjs/mongoose";

@Schema()
export class User {
  @Prop({ required: true })
  name: string;
  @Prop({ required: true, unique: true })
  username: string;
  @Prop({ required: true, unique: true })
  email: string;
  @Prop([String])
  interests: string[];
  @Prop({ default: Date.now })
  createdAt: Date;
}

export class UserDto {
  readonly name: string;
  readonly username: string;
  readonly email: string;
  readonly interests: string[];
  readonly createdAt?: Date;
}

export const UserSchema = SchemaFactory.createForClass(User);