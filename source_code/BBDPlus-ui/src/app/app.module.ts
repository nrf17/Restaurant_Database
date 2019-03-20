import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HttpClient } from '@angular/common/http';

import {TableModule} from 'primeng/table';
import {DropdownModule} from 'primeng/dropdown';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { BarDetailsComponent } from './bar-details/bar-details.component';
import { BeersComponent } from './beers/beers.component';
import { DrinkersComponent } from './drinkers/drinkers.component';
import { DrinkerDetailsComponent } from './drinker-details/drinker-details.component';
import { BeerDetailsComponent } from './beer-details/beer-details.component';
import { ManufacturersComponent } from './manufacturers/manufacturers.component';
import { ManufacturerDetailsComponent } from './manufacturer-details/manufacturer-details.component';
import { BartenderComponent } from './bartender/bartender.component';
import { BartenderDetailsComponent } from './bartender-details/bartender-details.component';
import { AnalyticsComponent } from './analytics/analytics.component';
import { ModifyComponent } from './modify/modify.component';
import {InputTextModule} from 'primeng/inputtext';
import {TabViewModule} from 'primeng/tabview';
import {TabMenuModule} from 'primeng/tabmenu';
import {PanelMenuModule} from 'primeng/panelmenu';
import {ButtonModule} from 'primeng/button';
import {ConfirmDialogModule} from 'primeng/confirmdialog';
import {PaginatorModule} from 'primeng/paginator';




@NgModule({
  declarations: [
    AppComponent,
    WelcomeComponent,
    BarDetailsComponent,
    BeersComponent,
    DrinkersComponent,
    DrinkerDetailsComponent,
    BeerDetailsComponent,
    ManufacturersComponent,
    ManufacturerDetailsComponent,
    BartenderComponent,
    BartenderDetailsComponent,
    AnalyticsComponent,
    ModifyComponent
  ],
  imports: [
    BrowserModule,
    TableModule,
    DropdownModule,
    BrowserAnimationsModule,
    HttpClientModule,
    AppRoutingModule,
    PaginatorModule,
    InputTextModule,
    TabViewModule,
    TabMenuModule,
    PanelMenuModule,
    ButtonModule,
    ConfirmDialogModule
  ],
  providers: [HttpClient],
  bootstrap: [AppComponent]
})
export class AppModule { }
