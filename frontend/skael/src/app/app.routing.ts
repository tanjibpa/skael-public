import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AuthGuard } from './core/auth';

import { LoginComponent, SignupComponent } from './pages/auth';
import { LayoutComponent } from './pages/layout';

export const routes: Routes = [
  {
    path: 'login', component: LoginComponent
  }, {
    path: 'signup', component: SignupComponent
  }, {
    path: '', component: LayoutComponent, canActivate: [AuthGuard],
    children: [
      {
        path: 'analytics', loadChildren: './pages/analytics/analytics.module#AnalyticsModule'
      }, {
        path: 'settings', loadChildren: './pages/settings/settings.module#SettingsModule'
      }, {
        path: '**', redirectTo: 'analytics'
      }
    ]
  }, {
    path: '**', redirectTo: '', pathMatch: 'full'
  }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes)],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
