import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'main.dart';

class BikeLocation{
  double latitude;
  double longitude;
  BikeLocation(double latitude, double longitude){
    this.latitude=latitude;
    this.longitude=longitude;
  }
}