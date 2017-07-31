import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router'

import { DxSparklineModule } from 'devextreme-angular'
import { MaterialModule } from '../../shared/material/material.module';
import { AnalyticsRoutingModule } from './analytics.routing.module';

import { AnalyticsComponent, BreadcrumbComponent, StatusComponent, SidebarComponent, PurchasesComponent } from '.';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    RouterModule,
    AnalyticsRoutingModule,
    MaterialModule,
    DxSparklineModule
  ],
  declarations: [
    AnalyticsComponent,
    BreadcrumbComponent,
    StatusComponent,
    SidebarComponent,
    PurchasesComponent
  ]
})
export class AnalyticsModule { }
