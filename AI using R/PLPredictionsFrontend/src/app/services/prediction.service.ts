import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PredictionService {

  predictMatchUrl = 'http://127.0.0.1:8000/predictions/?'

  constructor(
    private http: HttpClient
  ) { }

  predictMatch(homeTeam: string, awayTeam: string){
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers'
      })
    }
    console.log(this.predictMatchUrl+`homeTeam=${homeTeam}&awayTeam=${awayTeam}`);
    return this.http.get(this.predictMatchUrl+`homeTeam=${homeTeam}&awayTeam=${awayTeam}`,httpOptions);
  }
}
