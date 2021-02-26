import React, { createRef, useEffect, useRef, useState } from "react";
import styles from "../../styles/pages/Dashboard.module.css";
import NavBar from "../../components/NavBar";
import ApplicantCard from "../../components/ApplicantCard";
import { Container, Grid, Typography } from "@material-ui/core";

import ApplyPopover from "../../components/ApplyPopover";
import mockdata from "../../src/MockJob";
import PostJobDialog from "../../components/PostJobDialog";
import axios from "axios";

import { useRouter } from "next/router";

export default function DashBoard({ userInfo }) {
    const router = useRouter();
    const ref = useRef();
    const [logedIn, setLogedIn] = useState(true);
    const [jobData, setJobData] = useState(mockdata);
    // const [postOpen, setPostOpen] = useState(false);

    const childRef = createRef();

    const checkGreeting = () => {
        if (Date.now.getHours < 12) {
            return "Morning";
        } else if (Date.now.getHour < 18) {
            return "Afternoon";
        } else {
            return "Evening";
        }
    };

    const handleLogout = () => {
        setLogedIn(false);
        if (typeof window !== "undefined") {
            window.localStorage.removeItem("token");
        }
        router.push("/");
    };

    useEffect(() => {
        if (typeof window !== "undefined") {
            window.localStorage.getItem("token")
                ? setLogedIn(true)
                : setLogedIn(false);
            axios
                .get("http://localhost:8000/api/job", {
                    headers: {
                        Authorization: `JWT ${localStorage.getItem("token")}`,
                    },
                })
                .then((r) => {
                    console.log(r);
                    setJobData(r.data);
                })
                .catch((e) => {
                    console.log(e.response);
                });
        }

        if (!logedIn) {
            router.push("/login");
        }
    }, []);

    return (
        <>
            <NavBar
                toggleDrawer={childRef.toggleDrawer}
                handleLogout={handleLogout}
                jobData={jobData}
                setJobData={setJobData}
                isFaculty
            />

            <Container maxWidth="lg">
                <Typography
                    variant="h2"
                    component="h2"
                    gutterBottom
                    className={styles.greetingTitle}
                >
                    Good {checkGreeting()}!
                </Typography>
                <Grid container justify="center" spacing={5}>
                    <Grid item xs={12}>
                        <Typography variant="h4" component="h2" gutterBottom>
                            All Available Jobs
                        </Typography>
                    </Grid>
                    {jobData ? (
                        jobData.map((item) => {
                            return (
                                <Grid item xs={4}>
                                    <ApplyPopover ref={ref} />
                                    <ApplicantCard
                                        name={item.name}
                                        description={item.description}
                                        poster={item.poster}

                                        // handlePopover={ref.current.handleClick}
                                        // handlePopoverClose={ref.current.handleClose}
                                    />
                                </Grid>
                            );
                        })
                    ) : (
                        <div>Loading</div>
                    )}
                </Grid>

                {/* <JobCard
                name={"Undergruate Research"}
                description={"Looking for eager CS / CE / CSBA students looking to get involved in my Machine Learning Lab"}
                poster={"John Huh"}
              /> */}
            </Container>
        </>
    );
}
