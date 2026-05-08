import { BadGatewayException, BadRequestException, Body, Controller, Logger, Post, UnauthorizedException } from '@nestjs/common';
import { AuthService } from './auth.service';
import { UserLoginDto } from 'src/schemas/userlogin.schema';

@Controller('auth')
export class AuthController {
    private logger: Logger = new Logger(AuthController.name)
    constructor(private authService: AuthService) {
        
    }

    @Post('register')
    register(@Body() userLoginDto: UserLoginDto): Promise<any> {
        return this.authService.register(userLoginDto).then(result => {
            return { message: 'User registered successfully'};
        }).catch(err => {
            throw new BadRequestException({
                message: err.message || "Unknown error from server"
            })
        });
    }

    @Post('login')
    login(@Body() userLoginDto: UserLoginDto): Promise<any> {
        this.logger.debug('at login');
        return this.authService.login(userLoginDto).catch(err => {
            throw new BadGatewayException({
                errorType: err.type || "Type not specified",
                message: err.message || "Messsage not specified" 
            });
        });
    }
}
