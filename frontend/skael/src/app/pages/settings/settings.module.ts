import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { SettingsRoutingModule } from './settings-routing.module';
import { MaterialModule } from '../../shared/material/material.module';

import { SettingsComponent, ProfileComponent, UsersComponent, InviteUserModalComponent } from '.';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    MaterialModule,
    SettingsRoutingModule
  ],
  declarations: [
    SettingsComponent,
    ProfileComponent,
    UsersComponent,
    InviteUserModalComponent
  ],
  entryComponents: [
    InviteUserModalComponent
  ]
})
export class SettingsModule { }
