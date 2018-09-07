import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import {RouterModule} from '@angular/router';
import { NavbarComponent } from './navbar/navbar.component';
import { MatchComponent } from './match/match.component';
import { SeasonComponent } from './season/season.component';
import { AboutComponent } from './about/about.component';
import { HttpClientModule } from '@angular/common/http';

const appRoutes = [
  {
    path: '',
    redirectTo: 'about',
    pathMatch: 'full'
  },
  {
    path: 'about',
    component: AboutComponent
  },
  {
    path: 'match',
    component: MatchComponent
  },
  {
    path: 'season',
    component: SeasonComponent
  }
]

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    MatchComponent,
    SeasonComponent,
    AboutComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
