import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { LocationChangeListener } from '@angular/common';

// export interface Beer{
//   bar: string;
//   drinker : string;
//   count : string;
// }


@Injectable({
  providedIn: 'root'
})
export class BeersService {

  constructor(private http: HttpClient) { }

  getBeers(){
    return this.http.get<any[]>('/api/beer')
  }

  getBeer(beer:string){
    return this.http.get<any[]>('/api/beer/' + beer)
  }

  getConsumes(beer:string){
    return this.http.get<any[]>('/api/consume/' + beer)
  }

  gettimes(beer:string){
    return this.http.get<any[]>('/api/time/' + beer)
  }
  
}
