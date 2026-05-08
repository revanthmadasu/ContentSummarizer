import { BadRequestException, Injectable, Logger, UnauthorizedException } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { UserLogin, UserLoginDto } from 'src/schemas/userlogin.schema';
import * as bcrypt from 'bcrypt';
import { JwtService } from '@nestjs/jwt';

@Injectable()
export class AuthService {
    private logger: Logger = new Logger(AuthService.name);
    constructor(
        @InjectModel(UserLogin.name) private readonly userLoginModel: Model<UserLogin>,
        private jwtService: JwtService
    
    ) {}


    async register(userLoginDto: UserLoginDto): Promise<any> {
        this.logger.log('Registering user with data:', userLoginDto);
        const saltRounds = 10;
        const {email, password} = userLoginDto;
        const hashedPassword = await bcrypt.hash(password, saltRounds);
        const newUser = new this.userLoginModel({email, passwordHash: hashedPassword});
        return newUser.save();
    }

    async login(userLoginDto: UserLoginDto) {
        this.logger.debug('at login');
        const {email, password} = userLoginDto;
        const users: UserLogin[] = await this.userLoginModel.find({email}).exec();
        if (!users.length) {
            const error = {message: "Invalid user - user not found."};
            this.logger.error(error)
            throw new BadRequestException(error)
        }
        this.logger.debug(`user found: ${users.length}, password: ${users[0]?.passwordHash}`);
        const passwordMatch = await bcrypt.compare(password, users[0].passwordHash);
        if (passwordMatch) {
        this.logger.debug(`user password match`);
            const payload = {
                email
            };
            const jwtResponse = {
                access_token: await this.jwtService.signAsync(payload)
            };
            this.logger.debug(`jwt payload: ${jwtResponse.access_token}`);
            return jwtResponse;
        } else {
            this.logger.debug(`user password not match`);
            const error = {message: "user password not match"};
            this.logger.error(error)
            throw new UnauthorizedException(error);
        }
    }
}
