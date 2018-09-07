import {Component, OnInit, ViewChild} from '@angular/core';
import {PredictionService} from '../services/prediction.service';

@Component({
  selector: 'app-match',
  templateUrl: './match.component.html',
  styleUrls: ['./match.component.css']
})
export class MatchComponent implements OnInit {

  @ViewChild('homeTeam') homeTeam;
  @ViewChild('awayTeam') awayTeam;

  prediction: any

  toShowError = false;

  listOfTeams = [
    {
    apiName: 'Man City',
    dropdownName: 'Manchester City'
  },
    {
    apiName: 'Chelsea',
    dropdownName: 'Chelsea'
  },
    {
    apiName: 'Arsenal',
    dropdownName: 'Arsenal'
  },
    {
    apiName: 'Liverpool',
    dropdownName: 'Liverpool'
  },
    {
    apiName: 'Man United',
    dropdownName: 'Manchester United'
  },
    {
    apiName: 'Tottenham',
    dropdownName: 'Tottenham Hotspur'
  },
    {
    apiName: 'Everton',
    dropdownName: 'Everton'
  },
    {
    apiName: 'Southampton',
    dropdownName: 'Southampton'
  },
    {
    apiName: 'Newcastle',
    dropdownName: 'Newcastle United'
  },
    {
    apiName: 'Leicester',
    dropdownName: 'Leicester City'
  },
    {
    apiName: 'Fulham',
    dropdownName: 'Fulham'
  },
    {
    apiName: 'West Ham',
    dropdownName: 'West Ham United'
  },
    {
    apiName: 'Crystal Palace',
    dropdownName: 'Crystal Palace'
  },
    {
    apiName: 'Bournemouth',
    dropdownName: 'Bournemouth'
  },
    {
    apiName: 'Burnley',
    dropdownName: 'Burnley'
  },
    {
    apiName: 'Watford',
    dropdownName: 'Watford'
  },
    {
    apiName: 'Brighton',
    dropdownName: 'Brighton and Hove Albion'
  },
    {
    apiName: 'Wolves',
    dropdownName: 'Wolverhampton Wanderers'
  },
    {
    apiName: 'Cardiff',
    dropdownName: 'Cardiff City'
  },
    {
    apiName: 'Huddersfield',
    dropdownName: 'Huddersfield Town'
  }];

  constructor(
    private predict: PredictionService
  ) { }

  ngOnInit() {
    this.listOfTeams.sort();
  }

  onPredictClick() {
    // console.log(this.homeTeam.nativeElement.value);
    // console.log(this.awayTeam.nativeElement.value);

    let homeTeamName = this.homeTeam.nativeElement.value;
    let awayTeamName = this.awayTeam.nativeElement.value


    this.toShowError = homeTeamName === awayTeamName;

    if(!this.toShowError){
      this.predict.predictMatch(homeTeamName, awayTeamName).subscribe(
        prediction => this.prediction
      );

      console.log(this.prediction);
    }
  }

}
