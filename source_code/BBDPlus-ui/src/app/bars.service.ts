import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { LocationChangeListener } from '@angular/common';



export interface Bar{
  name: string;
  open : string;
  close : string;
  license : string;
  phone : string;
  address : string;
  city : string;
  state : string; 
}

@Injectable({
  providedIn: 'root'
})

export class BarsService {

  constructor(
    public http: HttpClient
  ) { }

  getBars(){
    return this.http.get<Bar[]>('/api/bar');
  }

  getBar(bar: string){
    return this.http.get<Bar>('/api/bar/' + bar)
  }

  getbarlarSpenders(bar: string){
    return this.http.get<any[]>('/api/larspender/' + bar)
  }

  gettoptenbrand(bar: string){
    return this.http.get<any[]>('/api/toptenbrand/' + bar)
  }

  gettimedistr(bar: string){
    return this.http.get<any[]>('/api/timedistr/' + bar)
  }

  getbusiestdays(bar:string){
    return this.http.get<any[]>('/api/busiestdays/' + bar)
  }
  
  getfractionsold(bar: string){
    return this.http.get<any[]>('/api/fractionsold/' + bar)
  }

 
}
