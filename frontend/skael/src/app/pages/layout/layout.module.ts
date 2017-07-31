import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { MaterialModule } from 'app/shared/material/material.module';

import { LayoutComponent, NavbarComponent } from '.';

@NgModule({
  imports: [
    CommonModule,
    RouterModule,
    MaterialModule
  ],
  declarations: [
    LayoutComponent,
    NavbarComponent
  ]
})
export class LayoutModule { }
