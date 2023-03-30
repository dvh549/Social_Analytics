<template>
<!-- Area Chart -->
                        <div class="col-xl-8 col-lg-7">
                            <div class="card shadow mb-4">
                                <!-- Card Header - Dropdown -->
                                <div
                                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                                    <h6 class="m-0 font-weight-bold text-primary">Correlation: Work From Home</h6>
                                </div>
                                <!-- Card Body -->
                                <div class="card-body" style="height:1400px">
                                    <div class="chart-area">
                                      <apexchart type="heatmap" height="1300px" :options="options" :series="corr_yes"></apexchart>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Pie Chart -->
                        <div class="col-xl-4 col-lg-5">
                            <div class="card shadow mb-4">
                                <!-- Card Header - Dropdown -->
                                <div
                                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                                    <h6 class="m-0 font-weight-bold text-primary" >Explaination</h6>
                                </div>
                                <!-- Card Body -->
                                <div class="card-body" style="height:1400px">
                                    <div class="chart-pie pt-4 pb-2">
                                        <p>According to the heatmap generated from the correlation analysis, for cluster 0, the “50s age group” has the highest correlation to it, followed by “kids”, supporting our cluster analysis that it consisted of people wanting to work from home since they had kids. For cluster 1, we see the highest correlation between it and the “20s age group” which supports our cluster analysis that cluster 1 consists of people in their 20s who are focused on work-life balance and quality time (very likely with their kids due to “kids” being the second highest correlated variable to cluster 1).<br>
                                          The highest correlated pair, excluding the correlation plotted with clusters, was found between the variables "better work-life balance and quality time" with a value of 0.823. This result suggests that people who prefer to work from home are seeking better work-life balance and quality time. The second-highest correlated pair is the "50s age group" and "business" with a value of 0.725. We believe that this may be due to the fact that people in their 50s are of a certain managerial level and can afford to work from home to handle and manage their respective business teams. The third-highest correlated pair was observed between "better sleep" and "better work-life balance" with a value of 0.674. This is very likely since better sleep arises from better work-life balance, where one is more at ease as opposed to being stressed because of work. <br>
                                          The heatmap generated from the correlation analysis revealed the lowest correlated pair, excluding the correlation plotted with clusters, between the "50s age group" and the "20s age group" with a value of -0.82. This could be because both age groups have different needs and goals when it comes to their career and lifestyle preferences. The second-lowest correlated pair was found between the "20s age group" and "kids" with a value of -0.69. Children are unlikely to be the reason why those in their 20s would want to work from home because they will be more focused on their careers. The third-lowest correlated pair was observed between the "50s age group" and "job opportunity" with a value of -0.63. This could be because people in their 50s already have stable careers and are looking to retire which may be why they prefer to work from home to acclimatise to a more relaxed environment before retirement.
                                        </p>
                                    </div>
                                    
                                </div>
                            </div>
                        </div>
</template>

<script>
export default {
  name: 'corr_wfh',
  props: {
    options: Object,
    corr_yes: Array
  }
}
</script>

