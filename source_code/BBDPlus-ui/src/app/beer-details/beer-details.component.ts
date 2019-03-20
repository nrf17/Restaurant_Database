import { Component, OnInit } from '@angular/core';
import { BeersService  } from '../beers.service';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';

@Component({
  selector: 'app-beer-details',
  templateUrl: './beer-details.component.html',
  styleUrls: ['./beer-details.component.css']
})
export class BeerDetailsComponent implements OnInit {

  beerName : string;
  beerDetails: any[];
  beerConsumes: any[];
  beerTimes: any[];

  constructor(
    private beerService: BeersService,
    private route: ActivatedRoute
  ) { 
    route.paramMap.subscribe((paramMap) => {
    this.beerName = paramMap.get('beer');
    beerService.getBeer(this.beerName).subscribe(
      data =>{
        this.beerDetails = data;
      },
      (error: HttpResponse<any>) => {
        if (error.status === 404){
          alert('Beer not found');
        }
        else{
          console.error(error.status + '-' + error.body);
          alert('error occurred on the server. please check the browser console');
        }
      }
     );
     beerService.getConsumes(this.beerName).subscribe(
      data =>{
        this.beerConsumes = data;
      });
    
      beerService.gettimes(this.beerName).subscribe(
        data =>{
          this.beerTimes = data;
        });
    }
  );}

  ngOnInit() {
  }

}
