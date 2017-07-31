import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'
import { RouterModule } from '@angular/router';

import { MaterialModule } from 'app/shared/material/material.module';

import { LoginComponent, SignupComponent, VerifyComponent, AuthComponent } from '.';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    RouterModule,
    MaterialModule
  ],
  declarations: [
    LoginComponent,
    SignupComponent,
    VerifyComponent,
    AuthComponent
  ],
  exports: [
    LoginComponent,
    SignupComponent,
    VerifyComponent,
    AuthComponent
  ]
})
export class AuthModule { }
