import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
// environment
import { environment } from 'environments/environment';
// npm libraries
import { LocalStorageModule } from 'angular-2-local-storage';
import { CookieModule } from 'ngx-cookie';
import { DxSparklineModule } from 'devextreme-angular';
import 'hammerjs';
// routing module
import { AppRoutingModule } from './app.routing'
// outer modules
import { MaterialModule } from './shared/material/material.module';
import { AuthModule } from './pages/auth/auth.module'
import { LayoutModule } from './pages/layout/layout.module';
// root components
import { AppComponent } from './app.component';
// services
import { HttpHelperService, ApiRoutingHelperService } from './core/helpers'
import { AuthService, AuthGuard } from './core/auth';
import { SharedService } from './shared/services';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpModule,
    CookieModule.forRoot(),
    LocalStorageModule.withConfig({prefix: environment.localStorage.prefix, storageType: 'localStorage'}),
    MaterialModule,
    DxSparklineModule,
    AppRoutingModule,
    AuthModule,
    LayoutModule
  ],
  providers: [
    HttpHelperService,
    ApiRoutingHelperService,
    AuthService,
    AuthGuard,
    SharedService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
