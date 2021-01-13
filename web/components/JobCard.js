import React from "react";
import {
  Button,
  Card,
  CardActionArea,
  CardActions,
  CardContent,
  CardMedia,
  Grid,
  Typography,
} from "@material-ui/core";

const JobCard = ({ name, description, poster }) => {
  return (
    <React.Fragment>
      <Grid item xs={4}>
        <Card>
          <CardActionArea>
            <CardMedia
              component="img"
              alt="jobcard"
              height="140"
              image="../../assets/cs141+.png"
              title="JobCard"
            />
            <CardContent>
              <Typography gutterBottom variant="h5" component="h2">
                {name}
              </Typography>
              <Typography variant="body2" color="textSecondary" component="p">
                {description}
              </Typography>
              <Typography variant="body2" color="textSecondary" component="p">
                {poster}
              </Typography>
            </CardContent>
          </CardActionArea>
          <CardActions>
            <Button size="small" color="secondary">
              Apply
            </Button>
            <Button size="small" color="secondary">
              Detail
            </Button>
          </CardActions>
        </Card>
      </Grid>
    </React.Fragment>
  );
};

export default JobCard;