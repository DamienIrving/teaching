# The climate system and how it works

The most simple depiction of the current climate is the
[annual mean temperature and rainfall](https://github.com/DamienIrving/teaching/blob/master/utas/utas_climate_lecture.ipynb)
across the globe.

Why do these maps look the way they do?
- Why is most of the planet at a habitable temperature?
- Why are all the major deserts of the world located at a similar latitude north or south? 
- Why is it freezing cold in Newfoundland and Labrador but relatively mild in the UK?
- Why is it so much wetter on the west coast of Tasmania than the east?

To answer those questions and many more, we need to know how the climate system works...

## 1. Planetary energy balance

*See [NASA's estimate](https://science-edu.larc.nasa.gov/energy_budget/) of the planetary energy budget and a good summary from [Loubere (2012)](https://www.nature.com/scitable/knowledge/library/the-global-climate-system-74649049)*.

The climate system is powered by radiation from the sun.

This energy warms the planet, but the warming also causes Earth to start radiating energy back into space.
Ultimately, the temperature of the planet will be that at which energy absorbed balances energy lost.

The energy coming from the sun is principally in the shorter wavelengths,
while the energy emitted by Earth surfaces is in the longer wavelengths.
(The wavelengths are dictated by the temperature of the emitter:
Earth is cooler than the sun so it radiates at a longer wavelength).

In general terms, the energy absorbed by the Earth can be written as:  
`EI = (1 – a) * Ω/4`

where `a` is planetary albedo (0.31, this is the proportion of incoming radiation reflected to space and lost) and
`Ω` is the solar constant (about 1367 W m-2, the solar radiation reaching Earth).
We divide by four since the solar energy is spread over the surface of the planetary sphere.
The Earth intercepts a circular area of incoming sunlight,
and this area is spread over a sphere with the same radius as the circle
(area of circle / area of sphere of same radius = 0.25).

The Earth will absorb energy and heat, and as it heats, it will emit radiation.
The energy emitted depends on planetary temperature at the surface where radiation escapes to space.
For simplicity this can be taken as the upper part of the troposphere.

> **Troposphere**
>
> There are a number of named
> [levels of the atmosphere](https://robertcarrollweather.files.wordpress.com/2014/11/agburt01_09.jpg), 
> the lowest of which is called the troposphere.
> It contains more than 80% of the mass of the atmosphere,
> it's where most vertical motion and weather changes take place,
> and almost all of the water vapour is contained there.
> It's 15-18km high in the tropics and 8-10km at the poles.

Again in general terms, the energy emitted by the Earth can be written as:  
`EO = σ * T^4`

(T = temperature in Kelvin, σ = 5.67 x 10-8 J/m2 sec K^4)

The Earth's temperature reaches a balance, called a steady state, when the two equations match (`EI` = `EO`).
Under those conditions we can write an equation for planetary temperature.
`T^4 = [(1 – a) Ω] / 4σ` 

The solution for this equation with measured solar flux at the top of the atmosphere
yields a value of -19.2°C for average planetary temperature.
This estimate is close to observed conditions in the upper part of the troposphere,
but of course is much below the average temperature at sea or ground level (about 14°C).
Some factor is causing our climate to be nearly 35°C warmer than we can explain by considering
radiation from the sun alone...


## 2. Greenhouse effect

To explain the higher than expected temperature in the lower troposhere, 
we need to understand its chemical composition.

Dry air is mainly composed of: nitrogen (78%), oxygen (21%),
argon (1%) and to a lesser extent carbon dioxide (410 ppm or 0.041%).
The remaining fraction is made up of various trace constituents such as methane (1.8 ppm).

In addition, a highly variable amount of water vapour is present in the air.
This ranges from approximately 0% in the coldest part of the atmosphere to as much as 5% in moist and hot regions.
On average, water vapour accounts for 0.25% of the mass of the atmosphere.

A number of these gases are radiatively active, which means they absorb (and radiate) radiation at particular wavelengths.
Collectively these "greenhouse gases" are more-or-less transparent to the shortwave radiation from the sun,
but are somewhat opaque to the longwave radiation emitted from Earth's surface.

So we end up with a situation where the atmosphere is essentially heated from the bottom (i.e. by the longwave radiation)
and the upward/outgoing longwave radiation gets trapped and recycled in the lower atmosphere by greenhouse gases.
A habitable average surface temperature of 14°C is the result,
with a lapse rate (i.e. the rate at which the troposphere cools with height) of about 6.5°C/km.

By their percentage contribution to the greenhouse effect on Earth the four major gases are
water vapor (36–70%), carbon dioxide (9–26%), methane (4–9%) and ozone (3–7%).

> **Why is most of the planet at a habitable temperature?**
>
> Because of the Greenhouse effect.

### Global water cycle

*See [Bengtssen (2010)](https://iopscience.iop.org/article/10.1088/1748-9326/5/2/025202/meta) for a good summary figure of the global water cycle.*

*Much of the text here is taken from the
[USGS Fundamentals of the Water Cycle](https://www.usgs.gov/special-topic/water-science-school/science/fundamentals-water-cycle?qt-science_center_objects=0#qt-science_center_objects) page.*

So if water vapor and and carbon dioxide are the most influential Greenhouse gases,
we should stop for a second and consider the global water and carbon cycles. 

The water cycle technically has no starting point, but we'll begin in the oceans,
since that is where most of Earth's water exists.
The sun, which drives the water cycle, heats water in the oceans.
Some of it evaporates as vapor into the air.
Rising air currents take the vapor up into the atmosphere, along with water from evapotranspiration,
which is water transpired from plants and evaporated from the soil.
The vapor rises into the air where cooler temperatures cause it to condense into clouds.

Air currents move clouds around the globe, cloud particles collide, grow, and fall out of the sky as precipitation.
Some precipitation falls as snow and can accumulate as ice caps and glaciers
which can store frozen water for thousands of years. 
Snowpacks in warmer climates often thaw and melt when spring arrives,
and the melted water flows overland as snowmelt.
Most precipitation falls back into the oceans or onto land, where, due to gravity,
the precipitation flows over the ground as surface runoff.
A portion of runoff enters rivers in valleys in the landscape, with streamflow moving water towards the oceans.
Runoff, and groundwater seepage, accumulate and are stored as freshwater in lakes.
Not all runoff flows into rivers, though. 
Much of it soaks into the ground as infiltration.
Some water infiltrates deep into the ground and replenishes aquifers (saturated subsurface rock),
which store huge amounts of freshwater for long periods of time.

For every 1°C of warming, the atmosphere can hold 7% more water vapour (Clausius-Clapeyron equation).
This is one of many global warming positive feedbacks.

### Global carbon cycle

*The Science Learning Hub Pokapū Akoranga Pūtaiao has a good interactive [image](https://www.sciencelearn.org.nz/image_maps/3-carbon-cycle) depicting the carbon cycle.*

The global carbon cycle is usually thought to have four major carbon sinks/stores (in grey) 
interconnected by pathways/processes of exchange (blue). These stores are:  

* the atmosphere (carbon dioxide),
* the terrestrial biosphere (vegetation and non-living organic material, such as soil carbon),
* the oceans (which includes dissolved inorganic carbon and living and non-living marine biota),
* and the sediments (fossil fuels, sediments and rocks)

If we focus on the atmosphere, here are the pathways for carbon leaving:

* *Photosynthesis:* When the sun is shining, plants perform photosynthesis to convert carbon dioxide into carbohydrates, releasing oxygen in the process. Deforestation and land clearing reduce this mechanism of carbon dioxide removal from the atmosphere.
* *Ocean productivity:* In upper ocean areas of high productivity, organisms form tissue containing carbon, and some also form carbonate shells or other hard body parts. Phytoplankton (microscopic plants that live in the ocean) soak up carbon via photosynthesis. In warmer seas, organisms cannot produce carbonate shells at the same rate, and increasingly acidic seas dissolve shells, or make it difficult to create shelly material.

Some pathways exchange with the atmosphere in both directions:

* *Ocean surface exchange:* At the surface of the oceans towards the poles, seawater becomes cooler and CO2 is more soluble. Cold ocean temperatures favor the uptake of carbon dioxide from the atmosphere whereas warm temperatures can cause the ocean surface to release carbon dioxide. With seas warming this means CO2 is not so easily absorbed, and remains in the atmosphere.

Carbon can be released back into the atmosphere in many different ways:

* *Respiration:* Performed by plants and animals.
* *Decay:* Of animal and plant matter. Fungi and bacteria break down the carbon compounds in dead animals and plants and convert the carbon to carbon dioxide if oxygen is present, or methane if not. The melting permafrost is releasing large amounts of methane.
* *Burning fossil fuels*


## 3. Planetary energy *imbalance*

Of course, we can’t talk about the planetary energy balance, Greenhouse effect and carbon cycle
without quickly touching on the fact that greenhouse gas concentrations have risen markedly in recent decades. 

This is clearly evident in
[data from Cape Grim](https://www.csiro.au/en/Research/OandA/Areas/Assessing-our-climate/Latest-greenhouse-gas-data)
on Tasmania’s west coast, which is one of the three premier Baseline Air Pollution Stations in the
World Meteorological Organization-Global Atmosphere Watch (WMO-GAW) network.
Pre-industrial CO2 concentrations (i.e. prior to the mid-1800s) were 280ppm, now we’re at almost 410ppm.

This increase in the Greenhouse effect means that there’s currently more energy coming into the system
than going out (i.e. an energy imbalance).
If Earth were like Mercury, for instance, a planet composed of low conductivity material and without oceans,
its surface temperature would rise quickly to a level at which the planet was again radiating
as much heat energy to space as the absorbed solar energy.
Earth's temperature does not adjust as fast as Mercury's due to the ocean's thermal inertia,
which is substantial because the ocean is mixed to considerable depths by winds and convection.
Thus it requires centuries for Earth's surface temperature to respond fully to a climate forcing
(i.e. even if we stopped emitting greenhouse gases today, the planet would continue to warm).

> **350.org**
>
> Interestingly, the name for the famous climate action organization [350.org](https://350.org/)
> comes from a [research paper](https://www.giss.nasa.gov/research/briefs/hansen_16/)
> published back in 2011 which suggested that atmospheric carbon dioxide must be reduced
> to about 350 ppm or less to stop global warming.
> (i.e. the planet has already warmed a bit in response to the energy imbalance - 1°C at the surface on average -
> hence the number is 350ppm and not 280ppm). 


## 4. General circulation

### Differential heating and the Hadley, Ferrel and Polar cells

*See [Loubere (2012), Figure 4 and associated text](https://www.nature.com/scitable/knowledge/library/the-global-climate-system-74649049) for a description of the circulation cells.*

An important detail we haven't addressed so far is that the surface heating by the sun is uneven.
Much more heat is absorbed at low than at high latitudes, 
because Earth's surface gradually tilts away from the sun.
In other words, the average angle of incidence of solar radiation across the year
gradually decreases from the tropics towards the poles.

> **Seasons**
>
> *Check out [these images](https://allgeographynow.wordpress.com/2016/02/22/the-earths-revolution-around-the-sun/) of Earth's orbit for the various seasons.*
>
> Earth's axis is tilted at 23.5°.
>
> At the equinox (March 21 and September 23) the sun is directly overhead at the equator.
>
> At the winter solstice (June 21) the sun is directly overhead at Tropic of Capricorn (23.5° South)
> and it's dark all day within the Arctic Circle (66.5° North). 
>
> At the summer solstice (December 22) the sun is directly overhead at the Tropic of Cancer (23.5° North)
> and it's dark all day within the Antarctic Circle (66.5° South)

This means that at low latitudes Earth's surface actually absorbs more energy
than the upper atmosphere emits to space (an energy surplus)
while at high latitudes the reverse is true (an energy deficit). 

Of course, absorbing more energy than is lost at low latitudes,
and the reverse closer to the poles, is not sustainable.
There has to be a balancing so that temperatures stabilise across the planet,
and this requires a transfer of heat from the equatorial region to higher latitudes.
The transfer is done by large scale motions in the atmosphere and oceans.
These motion (i.e. winds and currents) happen because the solar heating
and heat loss to space, create pressure gradients. 
Air and water move from high to low pressure conditions.

With respect to the atmospheric heat transport,
the strong heating of the bottom of the atmosphere in the tropics
makes the air less dense, so it becomes buoyant and rises (think hot air balloon).
This rising, lower density air in the tropics forms the largest vertical motion in the atmosphere.
From the tropics the rising air spreads poleward at altitude and loses heat to space by radiation.
The cooling causes density to increase and the air sinks.

On a planet that isn't rotating,
a single circulation cell would extend all the way to the poles in either hemisphere.
However, because of the Earth’s rotation, such an atmospheric structure would be unstable.
There are in fact three cells in either hemisphere named Hadley, Ferrel and Polar.

> **Precipitation vs evaporation**
>
> Earlier we looked at the global water cycle and noted that most of the evaporation and precipitation happens over the ocean.
> The atmospheric circulation cells cause a distinct pattern of precipitation and evaporation dominated regions to occur,
> as described by [The Global Water Cycle](https://www2.whoi.edu/site/globalwatercycle/) page 
> at the Woods Hole Oceanographic Institution website.
>
> This pattern is amplifying with global warming.
> You'll hear people talking about a general pattern across the globe of wet regions getting wetter,
> and dry regions getting drier.

> **Why are all the major deserts of the world located at a similar latitude north or south?**
>
> The ascending branch of the Hadley cell in the tropics is associated with
> low atmospheric surface pressure and high rainfall.
> As the air rises it cools and the water vapour in it condenses, forming clouds and ultimately rain.
> Having lost most of its water vapour to condensation and rainfall in the upward branch
> of the Hadley cell circulation, the descending air is dry and creates a region of higher pressure.
> The subtropical regions are therefore relatively free of the thunderstorms
> that are common in the tropics. 
> Many of the world's deserts are located in these subtropical latitudes.

### Coriolis effect

*A nice illustration of the Coriolis effect can be found [here](https://photobucket.com/gallery/user/henryflowers33/media/bWVkaWFJZDozMTc5NDIxMw==/?ref=).*

One might expect the surface winds associated with the Hadley cells to flow
from the two high pressure regions in the subtropics (i.e. there's one in each hemisphere)
in a north/south direction towards the equator.

In reality, the flow of the winds is modified by the fact
that this motion is happening over a rotating surface.
The Earth spins to the east and the speed of that rotation at the surface
is fastest at the equator and drops to zero at the poles.
That's because the speed depends on the distance which has to be covered in each daily rotation
(about 40,000 kms at the equator and zero at the poles;
so the rotational speed varies from about 1,690 to 0 km/hr)..

So, winds blowing to lower latitude get left behind
as they rotate eastward at a lower speed than the surface they are traveling over
(remember that rotation speed increases towards the equator).
This, called the Coriolis Effect, causes winds blowing to the equator to turn towards the west.
The result is a steady wind stream between 10 and 15° of latitude.
These are the tradewinds (also called the Easterlies, as in coming from the East).

Poleward of the high pressure center near 30° latitude,
the inverse of the trades is generated because air flowing poleward
moves over a surface which is rotating at slower and slower speeds.
In this case, the winds veer to the east as their eastward motion outstrips
that of the surface they are flowing over.
In this way a steady flow from west to east (the Westerlies) associated with the Ferrel cell
is created at about 45° latitude.  

> **Why does our weather in Hobart tend to come from the west?**
>
> Due to the mid-latitude westerlies that arise due to the Ferrel cell and Coriolis force.

### Mid-latitiude eddies

In the tropics,
the Hadley cell is the major mechanism by which the energy from the sun is transported polewards.
The Ferrel cell does some of the poleward heat transport in the mid-latitudes,
but the major mechanism is [eddies](https://earth.nullschool.net) embedded in the westerlies.
(Similar to stirring a cup of coffee,
the atmospheric stirring induced by the eddies evens out the temperature gradient between north and south.)
In other words, the high and low pressure systems we see on
[weather maps](http://www.bom.gov.au/australia/charts/) are collectively
doing the bulk of the poleward energy transport in the mid latitudes.
As air moves from the high pressure systems towards low pressure systems,
it is deflected by the coriolis force,
thus the wind circulates anti-clockwise around a high and clockwise around a low
(in the Southern Hemisphere).

> **Why is Melbourne famous for experiencing four seasons in one day?**
>
> Melbourne has a reputation (especially among people who live further north on the mainland)
> for having highly variable weather.
> This is because of its location in the mid-latitudes,
> where high and low pressure systems are spinning around all over the place
> (generally following a path from west to east).
> In summer, a low pressure system could move over Melbourne,
> with northerly winds bringing warm air from over central Australia
> as the system approaches from the west,
> and southerly winds bringing cold air from over the Southern Ocean
> as it departs to the east.

## 5. Scales of motion

Mid-latitude eddies are a good example of how smaller scale processes
can also have a large and important impact on the climate system.
Highs and lows in the mid-latitudes are "synoptic scale" features
(hundreds of kilometers across, last on the order of weeks)
and obviously much smaller than the Hadley cell,
but are collectively just as important for energy transport.

Smaller scale features are also very important in determining the local climate.
The influence of topography is obvious on global rainfall maps.
The trade winds are forced to rise over topography,
which causes the air to cool, condense and ultimately rain out.
By the time the air arrives on the downslope side of the topography,
it's realtively warm and dry.
This is known as the [foehn effect](http://www.atmo.arizona.edu/students/courselinks/fall12/atmo170a1s1/coming_up/week_9/lect27_regional_winds.html).

> **Why is Strahan much wetter than Swansea?**
>
> Due to the presence of the central highlands.
> Moist air in the westerlies is forced to rise and cool
> as it hits the west coast of Tasmania,
> which causes condensation and rain.
> By the time that air gets to the east coast, it's much drier.

At an even smaller scale, the afternoon
[sea breezes](https://www.swellnet.com/news/swellnet-analysis/2017/10/06/understanding-sea-breeze-part-1)
during summer in Sydney
(the land gets so hot it causes localised low pressure that
draws in air from over the relatively cool ocean)
means that the average maximum temperature in coastal suburbs 
like Bondi are substantially lower than for the inland western suburbs.


## 6. Ocean circulation

### Surface currents  
  
Turning out attention to the ocean,
the surface ocean currents arise due to a combination of the surface winds (i.e. the tradewinds and westerlies),
Earth's rotation (the Coriolis force) and Earth's landmasses.  
  
The surface winds blow over the oceans and the water responds to the friction and moves.
Of course, as the water begins to move, the Coriolis Effect comes into play
and the currents veer westwards if going to lower latitudes and easterwards if going poleward.
As a result, the surface ocean currents are driven in circles called
[gyres](https://www.nationalgeographic.org/encyclopedia/ocean-gyre/).
There are tropical, subtropical and polar gyres, 
the largest of which are the subtropical gyres that fill the middle of all oceans
and rotate such that poleward flow is on the western side of the basin.
Heat transfer from low to high latitudes is via the western boundary currents of the oceans
(like the Gulf Stream in the North Atlantic).

Just as with the scales of motion for the atmosphere,
there’s actually lots of small scale features embedded in the gyres,
as demonstrated by this [NASA perpetual ocean visualisation](https://www.youtube.com/watch?v=CCmTY0PKGDs).


> **Why is it freezing cold in Newfoundland and Labrador but relatively mild in the UK?**
>
> The Gulf Stream carries warm equatorial water up the eastern coast of the United States and on to western Europe,
> bypassing much of the eastern coastline of Canada.

### Thermocline

*For more information, check out the [NOAA ocean facts page on the thermocline](https://oceanservice.noaa.gov/facts/thermocline.html).*

These surface currents operate in a relatively thin upper layer of the sea which is heated by the sun.
This heating is kept relatively close to the ocean surface
because warming water makes it less dense and more resistant to sinking or mixing downwards.
The result is a barrier, called the thermocline, which develops particularly at lower and mid-latitudes
(it is more seasonal poleward) and that separates surface waters from the deep ocean.
The boundary, marked by a rapid downward temperature drop, usually occurs within a few hundred meters of less of the surface.
Below it, the greater mass of the oceans (down to an average depth of about 3800m) is cold and isolated from the winds.

### Deep ocean currents

*See Professor Matthew England's [recent projects page (Figure 2)](http://web.science.unsw.edu.au/~matthew/southern_ocean_variability.htm) for an illustration of deep water formation.*  

Despite its isolation from the surface, the deep sea is in motion.
Flow in the deep sea is initiated where the normal, density layered, oceanic water column breaks down
and surface water sinks due to processes which raise its density.
The primary cause of water column destabilization is sea-ice formation.
Making ice, which is fresh, leaves behind a brine which is quite salty.
This cold, highly saline (hence dense) water heads for the deep sea.
It supplies the great deep ocean water masses,
the North Atlantic Deep Water and Antarctic Bottom Water.

#### Coastal upwelling

*See the [CliMates blog post on upwelling](https://studentclimates.wordpress.com/2017/08/17/upwelling-zones-secrets-of-the-deep-ocean/) for a good overview.*

Naturally what goes down must come up if the deep currents are going to continue to flow. The process of these re-emerging deep water masses is called upwelling.

Upwelling doesn’t just happen anywhere but rather in certain regions of wind-sea interaction. Along the west coasts of continents in the southern hemisphere southerly winds (coming from the south east) are responsible for this phenomenon while in the northern hemisphere northerly winds cause upwelling. (Also, critically, the westerlies over the Sothern Ocean cause upwelling – see Matthew England's figure from the previous section.)

The force of the wind pushes the surface layer of the ocean to the north (in the southern hemisphere, and vice versa) however, due to the rotation of the earth the moving water masses are deflected to the left in the southern hemisphere and to the right in the northern hemisphere, so away from the west coasts. The missing surface waters are replaced by water masses from the depth by upwelling of former mentioned.

Usually, these rising waters are colder, nutrient and oxygen rich waters, leading to increasing numbers of phytoplankton when reaching the surface. Phytoplankton on the other hand forms the base of the food chain making upwelling regions the most productive fisheries of the world. About half the world’s total fish catch comes from upwelling zones.

### Global conveyor belt

Together, the surface currents and deep ocean currents form the
[Global Conveyor Belt](https://www.e-education.psu.edu/earth103/node/686),
which performs that fundamental task required of the ocean:
the transport of heat from the tropics towards the poles.

### Climate variability

Because it evolves more slowly than the atmosphere (and evaporation from the ocean surface is a massive source of moisture),
the ocean plays a big role in climate variability (i.e. in droughts, wetter/drier than average seasons/years, etc).

You'll notice in the latest [seasonal outlook](https://www.youtube.com/watch?v=XaWR-I4jvzE)
from the Bureau of Meteorology that they focus a lot on sea surface temperatures in the
tropical Indian Ocean (driven by the [Indian Ocean Dipole](http://www.bom.gov.au/climate/iod/))
and tropical Pacific Ocean (driven by the [El Nino Southern Oscillation](https://www.youtube.com/watch?v=dzat16LMtQk)).


## 7. Geologic perspective

To finish, it's useful to put the current climate (and climate change) in perspective
by considering how Earth’s climate has varied of it’s 4.6 billion year history.

Climate communication is a bit of a focus for this subject and we’ve just seen how the Bureau of Meteorology do it, 
so check out the [History of Earth's Climate](https://www.youtube.com/watch?v=dC_2WXyORGA) from SciShow,
which is one of the most popular science channels on YouTube.


## 8. Summary

Our weather and climate is driven ultimately by the unequal distribution
of energy that the Earth receives from the Sun.
The poleward transport of energy from the tropics,
combined with the rotation of the earth
(and also the configuration of the continents and ocean basins),
dictates the major features of the climate system:
trade winds, ocean gyres, upwelling,
regions of large-scale convection (rain) and subsidence (desert), etc.
These features modify, and are themselves modified by,
processes happening at smaller time and space scales
(e.g. mid-latitude eddies, sea-breezes),
creating the myriad of different local climates
that people experience around the world.

It's hard enough understanding the interactions between
things happening at different time and space scales in a stable climate,
let alone one that's changing due to greenhouse gas emissions.
The rest of this course will look at how scientists go about doing just that.


