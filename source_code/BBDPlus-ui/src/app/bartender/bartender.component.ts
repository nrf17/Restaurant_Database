import { Component, OnInit } from '@angular/core';
import { BartenderService } from '../bartender.service';
import { ActivatedRoute } from '@angular/router';




@Component({
  selector: 'app-bartender',
  templateUrl: './bartender.component.html',
  styleUrls: ['./bartender.component.css']
})
export class BartenderComponent implements OnInit {

  bartenders: any[];

  constructor(
    private bartenderService: BartenderService,
    private route: ActivatedRoute
  ) { 
    this.bartenderService.getBartenders().subscribe(
    data => {
      this.bartenders = data;
    }
  ); 
}

  ngOnInit() {
  }

}
