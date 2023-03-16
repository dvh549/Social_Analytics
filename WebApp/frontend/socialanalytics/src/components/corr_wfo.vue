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
                                <div class="card-body" style="height:1000px">
                                    <div class="chart-area">
                                      <apexchart type="heatmap" height="900px" :options="options" :series="corr_yes"></apexchart>
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
                                <div class="card-body" style="height:1000px">
                                    <div class="chart-pie pt-4 pb-2">
                                        <p>
                                            According to the heatmap generated from the correlation analysis, for cluster 0, the “40s age group” has the highest correlation to it, followed by “Tutor”, supporting our cluster analysis that it consisted of people having to work from office not because they want to but because they must. For cluster 1, we see the highest correlation between it and “RM_lazy”, followed by the “20s age group”, which supports our cluster analysis that cluster 1 consists of people in their 20s who are focused on climbing the corporate ladder and would feel lazy if they chose to work from home, and potentially affect their chances for promotion/career advancements.
                                            <br>The highest correlated pair, excluding the correlation plotted with clusters, was found between "productivity" and "saving money" with a value of 0.74. This could suggest that those working from office consider productivity as being to save the most amount of money. The second-highest correlated pair was found between the "40s age group" and "tutoring" with a value of 0.725. We believe that tutors in their 40s must work from the office because their offices are where their tutees are located at, and it is in no way an indication of their preference. The third-highest correlated pair was observed between the "20s age group" and "laziness" with a value of 0.674. It is likely that those in their 20s are motivated to work from office because they are afraid of becoming lazy when working from home, which could affect their career advancements and opportunities. 
                                            <br>The heatmap generated from the correlation analysis revealed the lowest correlated pair, excluding clusters, was between the "40s age group" and the "20s age group" with a value of -0.96. This could be because both age groups have different needs and goals when it comes to their career and lifestyle preferences. The second-lowest correlated pair was found between "male" and "productivity" with a value of -0.78, showcasing that productivity is unlikely to be the reason why males choose to work from the office, and could signal other intentions. The third-lowest correlated pair was observed between "better sleep" and "stress" with a value of -0.73. When one is stressed, it is very unlikely that they will be able to experience better sleep, and this could be a result of choosing to work from office and then possibly taking their work home. 

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

