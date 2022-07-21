# How to contribute

If you wish to contribute by adding or updating a satellite or a downlink, the best way would be making a pull request with your changes already in the form of a .json file. Below this section you can see an example of the key-value pairs used as well as their brief descriptions.

If you can't submit a pull request you can also open an issue describing the changes you think should be done to the database.

For a downlink to be added, all of the default key-values have to be filled out, only exceptions being "modulation" and "symrate" in case of things like non-regenerative transponders where they do not strictly apply.

The downlink also has to be **actively utilized**, even if it is only operated extremely sparsely. For example, the ISS SSTV downlink is eligible to be added, even though it is only used a few days per year. NOAA-19's 137.9125 MHz backup APT downlink is not eligible, even though the satellite is equipped with the hardware and is technically capable of transmitting at that frequency.

If a satellite is retired or the use of a specific downlink is ended, it should be removed from the database (after it is confirmed beyond reasonable doubt).

If you do submit a pull request or open an issue with proposed changes to the database, you should also include a source of the information. The preferred source of downlink information should be either your own or someone else's verifiable radio observations. Even though satellite operators usually publish their frequency and modulations, very often these do not reflect reality. The goal of this database is to document real-world downlinks as well as their basic properties relevant to their amateur reception.
