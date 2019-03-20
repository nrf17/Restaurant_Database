import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BarsService, Bar } from '../bars.service';
import { HttpResponse } from '@angular/common/http';

declare const Highcharts: any;

@Component({
  selector: 'app-bar-details',
  templateUrl: './bar-details.component.html',
  styleUrls: ['./bar-details.component.css']
})
export class BarDetailsComponent implements OnInit {

  barName : string;
  barDetails : Bar;
  barTimeDistr : any[];
  barBusiestDays:any[];

  constructor(
    private barService: BarsService,
    private route: ActivatedRoute,
  ) { 
      route.paramMap.subscribe((paramMap) => {
      this.barName = paramMap.get('bar');
      barService.getBar(this.barName).subscribe(
       data =>{
         this.barDetails = data;
       },
       (error: HttpResponse<any>) => {
         if (error.status === 404){
           alert('bar not found');
         }
         else{
           console.error(error.status + '-' + error.body);
           alert('error occurred on the server. please check the browser console');
         }
       }
      );

      barService.getbarlarSpenders(this.barName).subscribe(
        data=>{
          const barlist = [];
          const spentlist= [];
  
          data.forEach(barvar => {
            barlist.push(barvar.drinker)
            spentlist.push(barvar.spend)
          });
  
          this.renderChart1(barlist,spentlist);
        }
      );

      barService.gettoptenbrand(this.barName).subscribe(
        data=>{
          const manflist = [];
          const salelist= [];
  
          data.forEach(barvar => {
            manflist.push(barvar.manufacturer +" " +barvar.date)
            salelist.push(barvar.count)
          });
  
          this.renderChart2(manflist,salelist);
        }
      );
  
      barService.gettimedistr(this.barName).subscribe(
        data =>{
          this.barTimeDistr = data;
        });

        barService.getbusiestdays(this.barName).subscribe(
          data =>{
            this.barBusiestDays = data;
          });

        barService.getfractionsold(this.barName).subscribe(
          data=>{
            const itemlist = [];
            const fractionlist= [];
    
            data.forEach(barvar => {
              itemlist.push(barvar.item +" " +barvar.date)
              fractionlist.push(barvar.fsold)
            });
    
            this.renderChart3(itemlist,fractionlist);
          }
        );
    


    });
  }

  ngOnInit() {
  }


  renderChart1(drinker: string[], spender: number[]){
    Highcharts.chart('bargraph1', {
      chart: {
        type : 'column'
      },
      title: {
        text: 'Drinker that Spends the Most'
      },
      xAxis:{
        categories: drinker,
        title: {
          text: 'Drinker'
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
        drinker: {
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
        data: spender
      }]
    })
  }


  renderChart2(manufacturer: string[], sales: number[]){
    Highcharts.chart('bargraph2', {
      chart: {
        type : 'column'
      },
      title: {
        text: 'Top 10 Beer Brands'
      },
      xAxis:{
        categories: manufacturer,
        title: {
          text: 'Manufacturer'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Sales'
        },
        labels: {
          overflow: 'justify'
        }
      },
      plotOptions: {
        drinker: {
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
        data: sales
      }]
    })
  }

  renderChart3(item: string[], fractionsold: number[]){
    Highcharts.chart('bargraph3', {
      chart: {
        type : 'column'
      },
      title: {
        text: 'Fraction Sold'
      },
      xAxis:{
        categories: item,
        title: {
          text: 'Item'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Fraction Sold'
        },
        labels: {
          overflow: 'justify'
        }
      },
      plotOptions: {
        drinker: {
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
        data: fractionsold
      }]
    })
  }

}
