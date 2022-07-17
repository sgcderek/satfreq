# satfreq
Database of radio downlink frequencies used by satellites

***

# Example

## json file

    {
        "name": "Coriolis",
        "altnames": [
            "Coriolis/Windsat",
            "P98-2"
        ],
        "cospar": "2003-001A",
        "norad": 27640,
        "downlinks": [
            {
                "name": "WindSat",
                "frequency": 2221500000,
                "bandwidth": 1000000,
                "polarization": "RHC",
                "modulation": "BPSK",
                "symrate": 512000,
                "broadcast": true
            }
        ]
    }
    
## key-values

### satellite

`"name": "Coriolis"` - Name of the spacecraft  
`"altnames": ["Coriolis/Windsat", "P98-2"]` - Alternative names commonly used to refer to the spacecraft  
`"cospar": "2003-001A"` - COSPAR ID (International Designator) of the spacecraft  
`"norad": 27640` - NORAD ID (Satellite Catalog Number) of the spacecraft  
`"downlinks": [ ... ]` - List of active downlinks used by the spacecraft

### downlink

`"name": "WindSat"` - Name of the downlink  
`"frequency": 2221500000` - Center frequency of the downlink in Hz  
`"bandwidth": 1000000` - Bandwidth estimation of the downlink in Hz  
`"polarization": "RHC"` - Polarization of the downlink (see below)  
`"modulation": "BPSK"` - Modulation used by the downlink (if applicable, null if not)  
` "symrate": 512000"` - Symbol rate used by the downlink in symbols per second (if applicable, null if not)  
`"broadcast": true` - Whether the downlink is always active (see below)

### polarization
`"RHC"` - Right hand circular polarization  
`"LHC"` - Left hand circular polarization  
`"LIN"` - Linear polarization  
`"H"` - Horizontal polarization (geostationary only)  
`"V"` - Vertical polarization (geostationary only)  

Downlinks using polarization-division multiplexing are treated as two individual downlinks using orthogonal polarizations

### broadcast

A boolean value specifying whether the downlink is actively used by the satellite either all the time or based on a fixed temporal or spacial schedule. Minor service outages or changes are not considered.

**Examples:** 

***true:***
- NOAA-19 APT - downlink is always active
- Meteor-M N2-2 HRPT - downlink turns on during fixed time period (daylight)
- FengYun-3C HRPT - downlink turns on over a fixed area (Asia)
- Elektro-L N3 LRIT - downlink turns on according to a fixed time schedule

***false:***
- NOAA-19 GAC - time schedule available but not long-term predictable
- Proba-1 Payload Data - downlink only active after command from ground station
- ISS SSTV - downlink only on during specific events
