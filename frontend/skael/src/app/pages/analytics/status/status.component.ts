import { Component, OnInit } from '@angular/core';

export class CostInfo {
  month: number;
  2011: number;
  2012: number;
}

@Component({
  selector: 'skael-status',
  templateUrl: './status.component.html',
  styleUrls: ['./status.component.scss']
})

export class StatusComponent {

  purchaseTotal: CostInfo[] = [{
    month: 1,
    2011: 93,
    2012: 107
  }, {
    month: 2,
    2011: 90,
    2012: 112
  }, {
    month: 3,
    2011: 115,
    2012: 123
  }, {
    month: 4,
    2011: 116,
    2012: 123
  }, {
    month: 5,
    2011: 124,
    2012: 116
  }, {
    month: 6,
    2011: 115,
    2012: 102
  }, {
    month: 7,
    2011: 110,
    2012: 94
  }, {
    month: 8,
    2011: 117,
    2012: 105
  }, {
    month: 9,
    2011: 113,
    2012: 113
  }, {
    month: 10,
    2011: 103,
    2012: 111
  }, {
    month: 11,
    2011: 110,
    2012: 107
  }, {
    month: 12,
    2011: 109,
    2012: 110
  }];
}
