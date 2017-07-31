import { Component, OnInit } from '@angular/core';

import { Profile } from 'app/core/models';

@Component({
  selector: 'skael-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  profile: Profile = new Profile();

  constructor() { }

  ngOnInit() {
  }

  submit(): void {
    console.log(this.profile);
  }

}
