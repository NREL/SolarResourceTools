# Solar Resource Uncertainty (SOLARUN) Application
NREL provides solar resource data and tools to help energy system designers, project developers, renewable energy analysts, system operators, and others accelerate the integration of solar technologies on the grid. One of this tools is a GUI interface to calculate solar resource measurement uncertainty of various instruments. This tool includes source of uncertainties from calibration, zenith response, azimuth response, spectral response, tilt response, nonlinearity, temperature response, aging per year, datalogger, maintenance, etc.  For each source, there are 5 configuration options (acts on input / output quantity, uncertainty type, distribution, symmetry and analysis).

------------------

Original code by Aron Habte, Python translation by Rahul Gupta.

Based on publications:

- A. Habte, M. Sengupta, I. Reda, A. Andreas, J. Konings. "Calibration and Measurement Uncertainty Estimation of Radiometric Data: Preprint.": 9 pp. 2014. https://www.nrel.gov/docs/fy15osti/62214.pdf.
- Jorgen Konings, Aron Habte. "Uncertainty Evaluation of Measurements with Pyranometers and Pyrheliometers." Proceedings of SWC 2015: ISES Solar World Congress, 8-12 November 2015, Daegu, Korea: 11 pp. Freiburg, Germany: International Solar Energy Society (ISES). 2016. https://proceedings.ises.org/paper/swc2015/swc2015-0030-Konings.pdf.
- ASTM G213-17, Standard Guide for Evaluating Uncertainty in Calibration and Field Measurements of Broadband Irradiance with Pyranometers and Pyrheliometers, ASTM International, West Conshohocken, PA, 2017, www.astm.org
- https://midcdmz.nrel.gov/radiometer_uncert.xlsx