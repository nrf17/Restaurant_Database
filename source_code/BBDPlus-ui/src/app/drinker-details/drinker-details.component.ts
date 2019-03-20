import { Component, OnInit } from '@angular/core';
import { DrinkersService } from '../drinkers.service';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';

declare const Highcharts: any;


@Component({
  selector: 'app-drinker-details',
  templateUrl: './drinker-details.component.html',
  styleUrls: ['./drinker-details.component.css']
})
export class DrinkerDetailsComponent implements OnInit {

  drinkerName : string;
  drinkerDetails : any[];
  drinkerTrans: any[];

  constructor(
    private drinkerService: DrinkersService,
    private route: ActivatedRoute
  ) {route.paramMap.subscribe((paramMap) => {
    this.drinkerName = paramMap.get('drinker');
    drinkerService.getDrinker(this.drinkerName).subscribe(
     data =>{
       this.drinkerDetails = data;
     },
     (error: HttpResponse<any>) => {
       if (error.status === 404){
         alert('Dinker not found');
       }
       else{
         console.error(error.status + '-' + error.body);
         alert('error occurred on the server. please check the browser console');
       }
     }
    );
    drinkerService.getdrinkerTrans(this.drinkerName).subscribe(
      data=>{
        this.drinkerTrans = data;
      }
    );
    
    
    drinkerService.getdrinkerGraph1(this.drinkerName).subscribe(
      data=>{
        const beers = [];
        const counts= [];

        data.forEach(beer => {
          beers.push(beer.item)
          counts.push(beer.ordermost)
        });

        this.renderChart1(beers,counts);
      }
    );

    drinkerService.getdrinkerGraph2(this.drinkerName).subscribe(
      data=>{
        const barlist = [];
        const spentlist= [];

        data.forEach(barvar => {
          barlist.push(barvar.bar + " " + barvar.date)
          spentlist.push(barvar.spend)
        });

        this.renderChart2(barlist,spentlist);
      }
    );
    
    


  }); 
}

  ngOnInit() {
  }


  renderChart1(beers: string[], counts: number[]){
    Highcharts.chart('drinkergraph1', {
      chart: {
        type : 'column'
      },
      title: {
        text: 'Beers Ordered Most'
      },
      xAxis:{
        categories: beers,
        title: {
          text: 'Beer'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Purchased'
        },
        labels: {
          overflow: 'justify'
        }
      },
      plotOptions: {
        beer: {
          dataLabels: {
            enabled: true
          }
        }
      },
      legend:{
        enabled:false
      },
      credits:{
        enabled: false
      },
      series: [{
        data: counts
      }]
    })
  }

  renderChart2(beers: string[], counts: number[]){
    Highcharts.chart('drinkergraph2', {
      chart: {
        type : 'column'
      },
      title: {
        text: 'Spending on Different Bars'
      },
      xAxis:{
        categories: beers,
        title: {
          text: 'Bars and Dates'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Spent'
        },
        labels: {
          overflow: 'justify'
        }
      },
      plotOptions: {
        beer: {
          dataLabels: {
            enabled: true
          }
        }
      },
      legend:{
        enabled:false
      },
      credits:{
        enabled: false
      },
      series: [{
        data: counts
      }]
    })
  }

}
