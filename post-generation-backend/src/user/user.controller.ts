import { BadRequestException, Body, Controller, Post } from '@nestjs/common';
import { UserService } from './user.service';
import { UserDto } from '../schemas/user.schema';

@Controller('user')
export class UserController {
    constructor(private userService: UserService) {}
    @Post()
    createUser(@Body() userDto: UserDto) {
        return this.userService.createUser(userDto).then(user => {
            console.log('creating user:', user);
            return user;
        }).catch(err => {
            console.error('Error creating user:', err);
            throw new BadRequestException('Failed to create user', err.message);
        });
    }
}
