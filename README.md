# satfreq
Database of radio downlink frequencies used by satellites

# How to contribute

If you wish to contribute by adding or updating a satellite or a downlink, the best way would be making a pull request with your changes already in the form of a .json file. Below this section you can see an example of the key-value pairs used as well as their brief descriptions.

If you can't submit a pull request you can also open an issue describing the changes you think should be done to the database.

For a downlink to be added, all of the default key-values have to be filled out, only exceptions being "modulation" and "symrate" in case of things like non-regenerative transponders where they do not strictly apply.

The downlink also has to be **actively utilized**, even if it is only operated extremely sparsely. For example, the ISS SSTV downlink is eligible to be added, even though it is only used a few days per year. NOAA-19's 137.9125 MHz backup APT downlink is not eligible, even though the satellite is equipped with the hardware and is technically capable of transmitting at that frequency.

If a satellite is retired or the use of a specific downlink is ended, it should be removed from the database (after it is confirmed beyond reasonable doubt).

If you do submit a pull request or open an issue with proposed changes to the database, you should also include a source of the information. The preferred source of downlink information should be either your own or someone else's verifiable radio observations. Even though satellite operators usually publish their frequency and modulations, very often these do not reflect reality. The goal of this database is to document real-world downlinks as well as their basic properties relevant to their amateur reception.

# Example

## json file

```json
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
                "description": "Real time WindSat sounder data",
                "frequency": 2221500000,
                "bandwidth": 1000000,
                "polarization": "RHC",
                "modulation": "BPSK",
                "symrate": 512000,
                "broadcast": true
            }
        ]
    }
```

## key-values

### satellite

- `"name": "Coriolis"` - Name of the spacecraft  
- `"altnames": ["Coriolis/Windsat", "P98-2"]` - Alternative names commonly used to refer to the spacecraft  
- `"cospar": "2003-001A"` - COSPAR ID (International Designator) of the spacecraft  
- `"norad": 27640` - NORAD ID (Satellite Catalog Number) of the spacecraft  
- `"downlinks": [ ... ]` - List of active downlinks used by the spacecraft

### downlink

- `"name": "WindSat"` - Name of the downlink  
- `"description": "Real time WindSat sounder data"` - Description of the downlink and its contents when applicable
- `"frequency": 2221500000` - Center frequency of the downlink in Hz  
- `"bandwidth": 1000000` - Bandwidth estimation of the downlink in Hz  
- `"polarization": "RHC"` - Polarization of the downlink (see below)  
- `"modulation": "BPSK"` - Modulation used by the downlink (if applicable, null if not)  
- `"symrate": 512000"` - Symbol rate used by the downlink in symbols per second (if applicable, null if not)  
- `"broadcast": true` - Whether the downlink is always active (see below)

### polarization
- `"RHC"` - Right hand circular polarization  
- `"LHC"` - Left hand circular polarization  
- `"LIN"` - Linear polarization  
- `"H"` - Horizontal polarization (geostationary only)  
- `"V"` - Vertical polarization (geostationary only)  

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
