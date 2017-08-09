$(document).ready(function() {
    onFormChanged();
    $("form").change(onFormChanged);

});

onFormChanged = function() {
    var form_data = getFormData();
    NProgress.configure({ showSpinner: false }).start(0.7);
    getRecommendations(form_data["context"], form_data["weights"], function(response) {
        console.log(response)
        NProgress.done();
        NProgress.remove();
        showRecommendations(response["recommenders"]);
        addSongs(response["songs"]);
    });
}

getFormData = function() {
    var context = [],
        weights = [],
        form_data = $("form").serializeArray();

    for (i = 0; i < 8; i++) {
        context.push(form_data[i].value)
    }
    for (i = 8; i < 11; i++) {
        weights.push(form_data[i].value)
    }
    return {
        "context": context,
        "weights": weights
    }
}

getRecommendations = function(context, weights, callback) {
    var context_string = context.join(","),
        weights_string = weights.join(","),
        base_url = "/recommend?";
    var url = base_url + "context=" + context_string + "&weights=" + weights_string;
    $.get(url, callback)
}

addSongs = function(tracks) {
    var wrapper = document.getElementsByClassName("songs")[0]
    wrapper.innerHTML = ""
    tracks.forEach(function(track) {
        iframe = '<iframe width="100%" height="120" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=' + track["uri"] + '&amp;color=ff5500&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false"></iframe>'
        wrapper.innerHTML = wrapper.innerHTML + iframe;
    })

}

showRecommendations = function(recommenders) {
    recommenders.forEach(function(recommender) {
        updateRecommender(recommender.name, recommender['recommendation'], recommender['is_reliable'])
    });

}
updateRecommender = function(classname, recommendation, is_reliable) {
    $("." + classname + " .mood").text(recommendation[2])
    $("." + classname + " .tempo").text(Math.round(recommendation[1]))
    $("." + classname + " .genre").text(recommendation[0])

    if (is_reliable == 1) {
        $("." + classname).removeClass("table-danger");
    } else {
        $("." + classname).addClass("table-danger");
        $("." + classname + " .genre").html($("." + classname + " .genre").text() + '<span class="badge badge-danger">Recommender is not used as input is not reliable.</span>')

    }

}