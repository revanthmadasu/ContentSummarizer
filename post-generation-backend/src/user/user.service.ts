import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { User, UserDto } from '../schemas/user.schema';
import { Model } from 'mongoose';

@Injectable()
export class UserService {
    constructor(@InjectModel(User.name) private readonly userModel: Model<User>) {}

    createUser(userDto: UserDto): Promise<User> {
        console.log('creating User');
        try {
            const createdUser = new this.userModel(userDto);
            return createdUser.save().then(user => {
                console.log('User created successfully:', user);
                return user;
            }).catch(err => {
                console.error('Error creating user:', err);
                throw err;
            });
        } catch (err) {
            console.error('Unexpected error in createUser:', err);
            throw err;
        }
    }

}
