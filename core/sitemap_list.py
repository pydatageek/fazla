from places.sitemap import (
    CountrySitemap, WorldSitemap
)
from sections.sitemap import (
    HomeSitemap, InfoSitemap, PageSitemap
)
from stats.sitemap import (
    CountryPopulationSitemap,
    CountryPopulationGrowthRateSitemap, CountryPopulationMedianAgeSitemap,
    CountryPopulationDensitySitemap, CountryPopulationFertilitySitemap,
    WorldPopulationSitemap,
    WorldPopulationGrowthRateSitemap, WorldPopulationMedianAgeSitemap,
    WorldPopulationDensitySitemap, WorldPopulationFertilitySitemap,
    CountryGdpSitemap, WorldGdpSitemap,
    CountryCovid19Sitemap, WorldCovid19Sitemap,
    CountryHdiSitemap, WorldHdiSitemap
)

sitemaps = {
    'home': HomeSitemap,

    'info': InfoSitemap,

    'world': WorldSitemap,
    'country': CountrySitemap,

    'world_covid19': WorldCovid19Sitemap,
    'country_covid19': CountryCovid19Sitemap,

    'world_population': WorldPopulationSitemap,
    'country_population': CountryPopulationSitemap,

    'world_gdp': WorldGdpSitemap,
    'country_gdp': CountryGdpSitemap,

    'world_hdi': WorldHdiSitemap,
    'country_hdi': CountryHdiSitemap,

    'world_population_growth_rate': WorldPopulationGrowthRateSitemap,
    'world_population_median_age': WorldPopulationMedianAgeSitemap,
    'world_population_density': WorldPopulationDensitySitemap,
    'world_population_fertility': WorldPopulationFertilitySitemap,

    'country_population_growth_rate': CountryPopulationGrowthRateSitemap,
    'country_population_median_age': CountryPopulationMedianAgeSitemap,
    'country_population_density': CountryPopulationDensitySitemap,
    'country_population_fertility': CountryPopulationFertilitySitemap,

    'page': PageSitemap,
}
