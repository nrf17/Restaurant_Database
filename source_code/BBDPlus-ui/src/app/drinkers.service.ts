import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DrinkersService {

  constructor(private http: HttpClient) { }

  getDrinkers(){
    return this.http.get<any[]>('/api/drinker')
  }

  getDrinker(drinker:string){
    return this.http.get<any[]>('/api/drinker/' + drinker)
  }

  getdrinkerTrans(drinker:string){
    return this.http.get<any[]>('/api/transaction/' + drinker)
  }

  getdrinkerGraph1(drinker:string){
    return this.http.get<any[]>('/api/drinkergraph1/' + drinker)
  }

  getdrinkerGraph2(drinker:string){
    return this.http.get<any[]>('/api/drinkergraph2/' + drinker)
  }
}
