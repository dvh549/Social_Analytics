<template>
<!-- Area Chart -->
                        <div class="col-xl-8 col-lg-7">
                            <div class="card shadow mb-4">
                                <!-- Card Header - Dropdown -->
                                <div
                                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                                    <h6 class="m-0 font-weight-bold text-primary">Cluster 1</h6>
                                </div>
                                <!-- Card Body -->
                                <div class="card-body" style="height:1400px">
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
                                <div class="card-body" style="height:1400px">
                                    <div class="chart-pie pt-4 pb-2">
                                        <p>
                                            Cluster 1 – This group are likely to be employees in their 20s striving to achieve the best in their respective professions where they are hyper-focused but also stressed. They prefer to work from office likely because they get lazy and unmotivated at home which would affect their job performances.
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

