#parks {
  polygon-fill: #66cca0;
  polygon-opacity: .4;
 }

#streets {
  [ST_TYPE = 'EXPY'] {
    ::case {
  	  line-color: #cccccc;
  	  line-width: 5;
      line-cap: round;
    }
    ::fill {
      line-color: #fff;
      line-width: 2.5;
    }        
  }
 }

#hydrology {
  polygon-fill: #72aed0;
}

#limits {
  polygon-fill: #e6e6e6;
  polygon-pattern-file: url(images/light_noise_diagonal.png);
  line-color: #cccccc;
  line-width: 2;
  line-offset: 2;
}

#schools {
  marker-file: url(images/maki/garden-24.svg);
  marker-fill: #359f73;
  marker-width: 30;
  marker-allow-overlap: true;
  marker-line-width: 1.0;
  marker-line-color: #fff;
}