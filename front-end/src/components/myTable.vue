<template>
    <div>
        <el-table :data="showPage"
                  tooltip-effect="light"
                  border>
            <el-table-column show-overflow-tooltip label="名称" min-width="40%"
                             prop="name"></el-table-column>
            <el-table-column show-overflow-tooltip label="状态" min-width="60%">
                <template slot-scope="scope">
                    <span :style="{color:getColor(scope.row)}">{{scope.row.status}}</span>
                </template>
            </el-table-column>
        </el-table>
        <div>
            <el-pagination
                    @current-change="handlePageChange"
                    :current-page="currentPage"
                    :page-size="pageSize"
                    layout="total, prev, pager, next"
                    :total=totalItem>
            </el-pagination>
        </div>
    </div>
</template>

<script>
    export default {
        name: "myTable",
        created() {
            //该例中数据在父组件拿到后才展示该组件部分、故可以放在created()中。正常应在数据更新后进行下列操作
            this.totalItem = this.tableData.length;
            let wholeTable = this.cloneObj(this.tableData);//编写时不希望组件内加一些编辑操作就会影响父页面数据；没有这个顾虑的话也可直接赋值
            this.allPages = [];
            for (let i = 0; i < wholeTable.length; i += this.pageSize) {
                this.allPages.push(wholeTable.slice(i, i + this.pageSize));
            }
            if (this.allPages.length > 0) {
                this.showPage = this.allPages[0];
            }
        },
        props: {
            //父组件传过来的参数
            tableData: {
                type: Array,
                default: () => {
                    return [];
                }
            },
        },
        data() {
            return {
                currentPage: 1,
                totalItem: 0,
                pageSize: 5,
                showPage: [],
                allPages: [],
            }
        },
        methods: {
            //由数据获取样式
            getColor(item) {
                let color = '#bbbbbb';
                switch (item.status) {
                    case '红色':
                        color = "#FF4949";
                        break;
                    case '蓝色':
                        color = "#3A8DE3";
                        break;
                    default:
                        color = '#bbbbbb';
                }
                return color;
            },
            //翻页操作
            handlePageChange(val) {
                this.currentPage = val;
                this.showPage = this.allPages[this.currentPage - 1];
            },
            //深度复制对象
            cloneObj(obj) {
                let newObj = {};
                if (typeof obj === 'object') {
                    if (obj instanceof Array) {
                        newObj = [];
                    }
                    for (var key in obj) {
                        let val = obj[key];
                        newObj[key] = (typeof val === 'object') ? this.cloneObj(val) : val;
                    }
                    return newObj;
                } else {
                    return obj;
                }
            },
        }
    }
</script>

<style>
</style>
