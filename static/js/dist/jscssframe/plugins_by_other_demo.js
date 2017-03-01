/**
 * Created by ysw on 2017-03-01.
 */
$(function () {
    $("body").scrollspy({
        target: "#menu",
        offset: 200
    })

    $("#menu_ul > li").click(function () {
        $(this).siblings().removeClass("active");
        $(this).addClass("active");
    })

    $("#datetimepicker").datetimepicker({
        format: "yyyy-mm-dd",  // 输出日期的格式
        weekStart: 1,  // 一周开始时间 0为周日
        startDate: new Date("2017", "0", "1"),  // 开始时间
        endDate: new Date(),  // 结束时间
        daysOfWeekDisabled: [0, 3],  // 设置不可选的星期 此处为周日和周三不可选
        autoclose: true,  // 选择完后关闭日历
        startView: 2,  // 打开后开始的视图 0 hour 1 day 2 month 3 year 4 decade
        minView: 2,
        maxView: 2,
        todayBtn: true,  // 今天按钮
        todayHighlight: true,  // 今天按钮高亮
        keyboardNavigation: true,  // 允许键盘选择
        language: "zh-CN",  // 语言
        minuteStep: 10,  // 选择分钟时的步进
        pickerPosition: "bottom-left",  // 日历出现在控件右边
        initialDate: new Date()
    });
    $("#datetimepicker_clear").click(function () {
        $("#datetimepicker").val("");
    });
    $("#datetimepicker_show").click(function () {
        $("#datetimepicker").datetimepicker("show");
    });

    $("#fileinput").fileinput({
        language: "zh",
        allowedFileExtensions: ["jpg", "png", "jpeg", "gif"],
        allowedFileTypes: ["image"],
        uploadUrl: "#",
        deleteUrl: "#",
        maxFileSize: 1000,  // 单个文件的大小 KB
        maxFileCount: 2,
        showClose: false,
        uploadAsync: false,  // 对于多个文件是否异步上传
        previewSettings: {
            image: {width: "auto", height: "90px"},
        },
    });

    $("#typeahead").typeahead({
        source: [
            "asd",
            "asdasd",
            "asdq",
            "阿斯顿",
            "asd",
            "asdasd",
            "asdq",
            "阿斯顿",
            "asd",
            "asdasd",
            "asdq",
            "阿斯顿"
        ],
        autoSelect: true,
        items: 5
    });

    $("#limarquee").liMarquee({
        direction: "left",
        loop: -1,
        scrolldelay: 0,
        scrollamount: 60,
        circular: true,  // 无缝滚动
        drag: true,  // 鼠标可拖动
        hoverstop: false,  // 鼠标悬停
    });

    var wang_editor = new wangEditor("wang_editor");
    wang_editor.create();
    $("#wang_editor_button").find("button").click(function () {
        switch ($(this).index()) {
            case 0:
                wang_editor.$txt.html("<p>要初始化的内容</p>");
                break;
            case 1:
                $("#wang_editor_textarea").val(wang_editor.$txt.html());
                break;
            case 2:
                $("#wang_editor_textarea").val(wang_editor.$txt.text());
                break;
            case 3:
                wang_editor.$txt.append("<p>要追加的内容</p>");
                break;
            case 4:
                wang_editor.clear();
                break;
            case 5:
                if ($("#wang_editor_container").find(".menu-item.clearfix").find("a.disable").length) {
                    wang_editor.enable();
                } else {
                    wang_editor.disable();
                }
                break;
            default:
                break;
        }
        ;
    });

    var slider = $("#unslider").unslider({
        autoplay: true,
        speed: 500,  // 滚动时间
        delay: 2000,  // 轮播间隔
        index: 0,   // 初始图片
        animation: "vertical",  // 动画 fade模式需要arrows flase 设置高度
        arrows: true,  // 左右箭头
        infinite: true,  // 循环
        key: false,  // 是否支持键盘
        nav: true,  // 是否有排序小点
    });
    $("#unslider_button").find("input").click(function () {
        switch ($(this).index()) {
            case 0:
                slider.data("unslider").prev();
                break;
            case 1:
                slider.data("unslider").next();
                break;
            case 3:
                slider.data("unslider").start();
                break;
            case 4:
                slider.data("unslider").stop();
                break;
            default:
                break;
        }
        ;
    });
    $("#unslider_button").find("input")[2].addEventListener("keydown", function () {
        $(this).val("");
    });
    $("#unslider_button").find("input")[2].addEventListener("keyup", function () {
        slider.data("unslider").animate($(this).val());
    });

    var hammer = new Hammer.Manager($("#hammer")[0], {});  // 手势管理
    hammer.add(
        new Hammer.Pan({
            direction: Hammer.DIRECTION_ALL,  // 拖动方向
            threshold: 50  // 阀值
        })
    );  // 拖动
    hammer.add(
        new Hammer.Tap({
            event: 'quadrupletap',
            taps: 2
        })
    );  // 多重点击
    hammer.add(
        new Hammer.Tap()
    );  // 点击
    hammer.add(
        new Hammer.Press()
    );  // 按压
    hammer.on("pan tap quadrupletap press", function (ev) {
        $("#hammer")[0].textContent = ev.type + " 触发";
    });
});