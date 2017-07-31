import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Router } from '@angular/router';

import { AuthService } from 'app/core/auth';

import { Auth, Error } from 'app/core/models';

@Component({
  selector: 'skael-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  @Output() onLogin: EventEmitter<any> = new EventEmitter();

  user: Auth = new Auth();
  rememberMe = false;
  isLoading = false;
  error: Error = new Error();

  constructor(
    private router: Router,
    private authService: AuthService
  ) { }

  ngOnInit() {
    this.user.username = '';
    this.user.password = '';
  }

  login(f): void {
    if (!this.user.username || !this.user.password) {
      this.error.isError = true;
      this.error.message = 'All fields are required.'
      return;
    }
    if (f.form.valid) {
      this.isLoading = true;
      this.error.isError = false;
      this.authService.login(this.user).subscribe((res) => {
        this.isLoading = false;
        if (res.success) {
          this.router.navigate(['/']);
          this.onLogin.emit();
        }
      }, (err) => {
        this.isLoading = false;
        this.error.isError = true;
        this.error.message = 'The username/password couple is invalid.';
      });
    }
  }

}
